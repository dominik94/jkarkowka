from django.contrib.auth.models import User
from api.models import Student, Question, Answer, SolvedTest, Test, Group, Lecturer, SubmittedAnswer
from rest_framework import serializers


class UserWithoutEmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class LecturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('name',)


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'content', 'good')


class HiddenAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'content')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'content', 'answers')


class ShortQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'content',)


class QuestionWithoutAnswerSerializer(serializers.HyperlinkedModelSerializer):
    answers = HiddenAnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'content', 'answers')


class TestSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ('id', 'key', 'name', 'questions')


class ShortTestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name')


class TestStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('id',)


class TestWithHiddenAnswersSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionWithoutAnswerSerializer(many=True)

    class Meta:
        model = Test
        fields = ('id', 'name', 'questions')


class SolvedTestSerializer(serializers.HyperlinkedModelSerializer):
    test = ShortTestSerializer(many=False)

    class Meta:
        model = SolvedTest
        fields = ('test', 'score', 'max')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    solved_tests = SolvedTestSerializer(many=True)

    class Meta:
        model = Student
        fields = ('user', 'solved_tests')


class StudentWithoutEmailSerializer(serializers.HyperlinkedModelSerializer):
    user = UserWithoutEmailSerializer()

    class Meta:
        model = Student
        fields = ('user',)


class StudentsInGroupSerializer(serializers.HyperlinkedModelSerializer):
    students = StudentWithoutEmailSerializer(many=True)

    class Meta:
        model = Group
        fields = ('students',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('id','name',)

