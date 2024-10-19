from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import VotingRoom, Candidate, Voter, Vote
from .serializers import VotingRoomSerializer, CandidateSerializer, VoterSerializer, VoteSerializer

class VotingRoomViewSet(viewsets.ModelViewSet):
    queryset = VotingRoom.objects.all()
    serializer_class = VotingRoomSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class VoterViewSet(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def create(self, request, *args, **kwargs):
        # Extract votes from the request
        votes_data = request.data.get('votes', [])
        voter_id = request.data.get('voter')

        # Validate that voter_id is not null
        if voter_id is None:
            return Response({'error': 'Voter ID must be provided.'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch voter instance
        try:
            voter = Voter.objects.get(id=voter_id)
        except Voter.DoesNotExist:
            return Response({'error': 'Voter does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure voter hasn't voted before
        if voter.has_voted:
            return Response({'error': 'Voter has already voted.'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure total votes count is exactly 10
        if sum(vote.get('votes_count', 0) for vote in votes_data) != 10:
            return Response({'error': 'Total votes must equal 10.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create votes
        for vote_data in votes_data:
            candidate_id = vote_data.get('candidate')
            votes_count = vote_data.get('votes_count')

            if candidate_id is None or votes_count is None:
                return Response({'error': 'Candidate ID and votes_count must be provided for each vote.'}, status=status.HTTP_400_BAD_REQUEST)

            candidate = Candidate.objects.get(id=candidate_id)
            Vote.objects.create(voter=voter, candidate=candidate, votes_count=votes_count)

        # Mark voter as having voted
        voter.has_voted = True
        voter.save()

        return Response({'success': 'Votes recorded successfully.'}, status=status.HTTP_201_CREATED)
