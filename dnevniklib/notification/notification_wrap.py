class NotificationWrap:


    @staticmethod
    def build(notifications):
        res_dict = dict()
        for notification in notifications:
            if notification.subject_name in res_dict.keys():
                res_dict[notification.subject_name].append(notification)
            else:
                res_dict[notification.subject_name] = [notification]

        res_str = ""
        for key, value in res_dict.items():
            res_str += f"\n{key}: \n"
            for mark in value:
                res_str += (str(mark) + '\n')
        return res_str
