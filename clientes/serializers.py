from rest_framework import serializers
from clientes.models import Cadastro


class CadastroSerializer(serializers.Serializer):
    nome = serializers.CharField()
    telefone = serializers.CharField()
    cpf = serializers.CharField()
    email = serializers.EmailField()
    data_de_aniversario = serializers.CharField()
    idade = serializers.IntegerField()

    def create(self, validated_data):
        cadastro_de_clientes = Cadastro.objects.create(**validated_data)
        return cadastro_de_clientes

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.telefone = validated_data.get('telefone', instance.telefone)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.emmail = validated_data.get('email', instance.email)
        instance.data_de_nascimento = validated_data.get('data_de_nascimento', instance.data_de_nascimento)
        instance.idade = validated_data.get('idade', instance.idade)
        instance.save()
        return instance
