from addboards.models import Ad, Review
from rest_framework import serializers


class AdSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели объявления (Ad).

    Атрибуты:
        model (Ad): Модель данных, которую сериализует этот сериализатор.
        fields ("__all__"): Все поля модели будут включены в сериализацию.
    """
    class Meta:
        model = Ad
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели отзыва (Review).

    Атрибуты:
        model (Review): Модель данных, которую сериализует этот сериализатор.
        fields ("__all__"): Все поля модели будут включены в сериализацию.
    """
    class Meta:
        model = Review
        fields = "__all__"
