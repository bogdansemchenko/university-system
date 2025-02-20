import pickle


class UniversityStorage:
    @staticmethod
    def save(university, filename='university_state.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(university, f)

    @staticmethod
    def load(filename='university_state.pkl'):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return None