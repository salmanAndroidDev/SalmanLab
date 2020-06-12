class Table:
    def __init__(self, path=None):
        pass

    def save(self, path):
        pass

    def get_row_dict(self, row_index):
        pass

    def get_cell(self, row_index, label):
        pass

    def get_column(self, label):
        pass

    def get_label_index(self, label):
        pass

    def to_dict(self):
        """
                format: {
                            "labels":[],
                            "rows":[[...],
                                    [...],
                                    .....
                                    .....
                                    [...]]
                        }
        """
        pass