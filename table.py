import camelot

def table_prc(file_path = "data/keppel-corporation-limited-annual-report-2018.pdf"):
    """Extract table from pdf"""
    pages = input("Enter the page number: ")
    try:
        tables = camelot.read_pdf(file_path, pages=pages, flavor='stream')
        print(tables)
        num = []
        for i in range(len(tables)):
            print(tables[i].df)
            num.append(i+1)
        ind = input("Select the position of the table you want to extract (1 or 2, or 3 etc): ")
        try:
            indx = int(ind)
            answer = tables[indx-1].df
            answer.to_csv('answer.csv')
            return answer
        except:
            print(f"Run function again and select from this option {num}")
    except ValueError:
        print("Incorrect page details")

table_prc()