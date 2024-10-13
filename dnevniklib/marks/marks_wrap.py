class MarksWrap:


    @staticmethod
    def build(marks):
        res_dict = dict()
        for mark in marks:
            if mark.subject_name in res_dict.keys():
                res_dict[mark.subject_name].append(mark)
            else:
                res_dict[mark.subject_name] = [mark]

        res_str = ""
        for key, value in res_dict.items():
            res_str += f"\n{key}: \n"
            for mark in value:
                res_str += (str(mark) + '\n')
        return res_str
