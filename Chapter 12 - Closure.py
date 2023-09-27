def interview_closure():
    user_ids = list(range(101, 151))

    def get_filtered_users():
        hasil = []
        for user_id in user_ids:
            if user_id % 5 == 0 and user_id % 2 == 0:
                hasil.append(user_id)
        return hasil

    return get_filtered_users


if __name__ == "__main__":
    interview_func = interview_closure()

    hasil = interview_func()

    print(hasil)
