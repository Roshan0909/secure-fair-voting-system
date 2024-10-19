from django.db import models

class VotingRoom(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    voting_room = models.ForeignKey(VotingRoom, on_delete=models.CASCADE, related_name='candidates')

    def __str__(self):
        return self.name

class Voter(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    voting_room = models.ForeignKey(VotingRoom, on_delete=models.CASCADE, related_name='voters')
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE, related_name='votes')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    votes_count = models.IntegerField()

    def __str__(self):
        return f'{self.voter} -> {self.candidate} : {self.votes_count}'
