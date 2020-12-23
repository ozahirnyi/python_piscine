from ex00 import FileLoader

fl_obj = FileLoader("/Users/ozahirnyi/PycharmProjects/pythonProject/d04/test.csv")
fl_obj.load()
fl_obj.display(fl_obj.file_data, -2)