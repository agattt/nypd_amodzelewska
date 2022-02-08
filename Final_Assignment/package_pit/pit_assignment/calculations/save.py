
def to_file(wrt, data_frame, sheet_name):

    data_frame.to_excel(wrt, sheet_name=sheet_name, index=False)
