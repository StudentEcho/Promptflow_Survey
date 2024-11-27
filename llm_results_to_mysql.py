from promptflow.core import tool
import mysql.connector
import uuid

@tool(input_schema={"data": "string"}, output_schema={"status": "string"})
def insert_data_into_mysql(data):
    # Connection details for MySQL
    host = ''
    database = ''
    user = ''  # Your Azure MySQL username
    password = ''  # Your Azure MySQL password
    
    status = ''
    
    # Generate a unique ID for each entry
    unique_id = str(uuid.uuid4())
    
    # Adjusting the split delimiter to match the input data format more reliably
    split_data = data.split("; ")
    task = None
    answer = None
    
    # Ensure split_data has at least two elements
    if len(split_data) >= 2:
        task = split_data[0].split("llmTask: ")[1] if "llmTask: " in split_data[0] else None
        answer = split_data[1].split("llmAnswers: ")[1] if "llmAnswers: " in split_data[1] else None

    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        print("Connection established successfully.")

        cursor = connection.cursor()

        # Update query to insert both llmTask and llmAnswers along with a unique ID
        update_query = """
        INSERT INTO surveytable (_id, llmTask, llmAnswers)
        VALUES (%s, %s, %s)
        """
    
        # Executing the insert query with unique_id, task, and answer
        cursor.execute(update_query, (unique_id, task, answer))

        # Committing the transaction
        connection.commit()
        print("Inserted llmTask and llmAnswers into the surveytable successfully.")
        status = 'Success'
        
    except mysql.connector.Error as ex:
        error_message = ex.msg
        print(f"Error message: {error_message}")
        status = 'Failed'
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")
    
    return {"status": status}

# Example usage
# if __name__ == "__main__":
#     unique_id = str(uuid.uuid4())
#     results = "llmTask: feedback sentiment analysis; llmAnswers: Positive feedback."
#     output = insert_data_into_mysql(unique_id, results)
#     print(output)