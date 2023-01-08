from rest_framework import serializers
from .models import Compania,Plan,Deducible

class CompaniaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compania
        fields = ["idCompania","nombreCompania","ruc","nombreCoordinador","celular","correo","is_active"]

class DeducibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deducible
        fields = "__all__"

class DeducibleDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deducible
        fields = ["idDeducible","is_active"]

class PlanSerializer(serializers.ModelSerializer):
    #compania=CompaniaSerializer()
    #deducible=DeducibleSerializer(many=True)
    deducibles=serializers.SerializerMethodField()
    companias=serializers.SerializerMethodField()
    class Meta:
        model = Plan
        fields = "__all__"
    def get_companias(self,obj):
        #companias=Compania.objects.all()
        companias=obj.idCompania
        response = CompaniaSerializer(companias).data
        return response
            
    def get_deducibles(self,obj): #obj=plan
        deducibles=Deducible.objects.filter(is_active=1,idPlan=obj.idPlan)
        response=DeducibleSerializer(deducibles,many=True)
        return response.data
         
class PlanPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"