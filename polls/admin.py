from django.contrib import admin
from .models import VotingRoom, Candidate, Voter, Vote

# Register each model to make them available in the Django admin
admin.site.register(VotingRoom)
admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(Vote)
