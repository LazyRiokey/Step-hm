from rest_framework.views import APIView
from rest_framework.response import Response
import random

# Create your views here.


class Oracle(APIView):
    def get(self, request):
        oracle_list = [
            "Предсказание 1", "Предсказание 2", 
            "Предсказание 3", "Предсказание 4", 
            "Предсказание 5", "Предсказание 6"]
        return Response({"oracle": oracle_list[random.randint(0, 5)]})

class RandomInt(APIView):

    def get(self, request):
        return Response({"rand_int": random.randint(0, 100)})

class RandomRangeInt(APIView):

    def post(self, request):
        start_range = request.data["start_range"]
        stop_range = request.data["stop_range"]

        if start_range and stop_range:
            result = random.randint(start_range, stop_range)
        else:
            result = "Что-то пошло не так.."

        return Response({"result": result})

class RandomListInt(APIView):

    def get(self, request):
        random_list = [random.randint(0, 100) for i in range(random.randint(0, 100))]
        return Response({"rand_range_list": random_list})