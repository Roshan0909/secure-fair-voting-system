from rest_framework import serializers
from .models import VotingRoom, Candidate, Voter, Vote

class VotingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotingRoom
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = '__all__'



class VoteSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all(), allow_null=False)
    votes_count = serializers.IntegerField(required=True)
    voter = serializers.PrimaryKeyRelatedField(queryset=Voter.objects.all(), allow_null=False)

    class Meta:
        model = Vote
        fields = '__all__'
    
    def validate(self, data):
        """
        Check that the total votes count is 10 for all votes provided in the request.
        """
        total_votes = sum(vote['votes_count'] for vote in self.initial_data.get('votes', []))
        if total_votes != 10:
            raise serializers.ValidationError("Total votes must equal 10.")
        return data
    
    def validate_voter(self, value):
        """
        Ensure that the voter has not voted before.
        """
        if value.has_voted:
            raise serializers.ValidationError("Voter has already voted.")
        return value
