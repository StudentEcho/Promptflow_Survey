from promptflow.core import tool
import mysql.connector

@tool(input_schema={"query": "string"}, output_schema={"results": "dict"})
def fetch_data_from_mysql(query):
    # Connection details
    host = 'wix-mysql-server-name.mysql.database.azure.com'
    database = 'mysqltutorial'
    user = 'shuzhennong'  # Your Azure MySQL username
    password = 'Fudan@0216$'  # Your Azure MySQL password

    # Initialize dictionaries to store results
    results_dict = {
        "Schools": [],
        "Grades": [],
        "Feedbacks": [],
        "Suggestions": []
    }
    
    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        print("Connection established successfully.")

        # Create a cursor object using the connection
        cursor = connection.cursor()

        # Execute the query
        print(f"Executing query: {query}")
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()
        print(f"Fetched {len(rows)} rows.")

        # Populate the dictionaries with data from each row
        for row in rows:
            if row[1]: results_dict["Schools"].append(row[1])
            if row[2]: results_dict["Grades"].append(row[2])
            if row[5]: results_dict["Feedbacks"].append(row[5])
            if row[6]: results_dict["Suggestions"].append(row[6])

    except mysql.connector.Error as ex:
        error_message = ex.msg
        print(f"Error message: {error_message}")
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")
    
    print(f"Results: {results_dict}")
    return {"results": results_dict}

# Example usage
if __name__ == "__main__":
    query = 'SELECT * FROM mysqltutorial.MicrosoftFormTable;'
    output = fetch_data_from_mysql(query)
    print(output)