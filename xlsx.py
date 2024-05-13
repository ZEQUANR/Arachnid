import pandas as pd


def read_table_to_objects(
    file_path: str, sheet_name: str = 0, engine: str = "openpyxl"
):
    if file_path.endswith(".xlsx") or file_path.endswith(".xls"):
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine=engine)
    elif file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        raise ValueError(
            "Unsupported file format. Only .xlsx, .xls, and .csv files are supported."
        )

    objects_list = df.to_dict("records")

    return objects_list


table_data = read_table_to_objects("A-share-main-board.xlsx", sheet_name="Sheet2")

print(table_data)
