# If missing values exist, print the column name and the number of missing values
def checkMissingValues(df):
    flag = False
    result = []
    for col in df.columns:
        if df[col].isna().any():
            flag = True
            result.append(str(col) + " " + str(df[col].isna().sum()))
    if flag:
        for item in result:
            print(item)
    return flag
