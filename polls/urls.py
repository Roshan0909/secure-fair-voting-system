from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VotingRoomViewSet, CandidateViewSet, VoterViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'voting-room', VotingRoomViewSet)
router.register(r'candidate', CandidateViewSet)
router.register(r'voter', VoterViewSet)
router.register(r'vote', VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
