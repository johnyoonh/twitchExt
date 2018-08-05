from statistics import mode


class VoteGetter:
    database = []
    def add_vote(name):
        self.database.append(name)

    def determine_winner():
        return mode(self.database)
