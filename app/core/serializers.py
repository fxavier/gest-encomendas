from rest_framework import serializers
from core.models import (Pessoa, Transportador, Remetente, Receptor, Viatura,
                         Rota, CategoriaCarga, TarifaPeso, TarifaVolume,
                         Servico, Carga)


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['nome', 'contacto']


class TransportadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportador
        fields = ['nome', 'contacto']


class RemetenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remetente
        fields = ['nome', 'contacto']


class ReceptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptor
        fields = ['nome', 'contacto']


class ViaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viatura
        fields = ['matricula']


class RotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rota
        fields = ['descricao']


class CategoriaCargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaCarga
        fields = ['descricao']


class TarifaPesoSerializer(serializers.ModelSerializer):
    nome_categoria_carga = serializers.StringRelatedField(source='categoria_carga')
    class Meta:
        model = TarifaPeso
        fields = ['rota', 'categoria_carga','nome_categoria_carga', 'valor_comercial', 'preco']


class TarifaVolumeSerializer(serializers.ModelSerializer):
    nome_categoria_carga = serializers.StringRelatedField(source='categoria_carga')
    class Meta:
        model = TarifaVolume
        fields = ['rota', 'categoria_carga','categoria_carga','valor_comercial', 'preco']


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['name', 'price']


class CargaSerializer(serializers.ModelSerializer):
    tarifa_peso_preco = serializers.SerializerMethodField()
    tarifa_volume_preco = serializers.SerializerMethodField()
    remetente_nome = serializers.StringRelatedField(source='remetente')
    remetente_contacto = serializers.SerializerMethodField()
    receptor_contacto = serializers.SerializerMethodField()
    receptor_nome = serializers.StringRelatedField(source='receptor')
    rota_descricao = serializers.StringRelatedField(source='rota')
    transportador_principal_nome = serializers.StringRelatedField(source='transportador_principal')
    transportador_secundario_nome = serializers.StringRelatedField(source='transportador_secundario')
    viatura_principal_matricula = serializers.StringRelatedField(source='viatura_principal')
    viatura_secundaria_matricula = serializers.StringRelatedField(source='viatura_secundaria')
    criado_por_nome = serializers.StringRelatedField(source='criado_por')
    modficado_por_nome = serializers.StringRelatedField(source='modificado_por')

    class Meta:
        model = Carga
        fields = ['codigo', 'descricao', 'valor_comercial', 'peso', 'volume',
                  'tarifa_peso', 'tarifa_peso_preco', 'tarifa_volume', 'tarifa_volume_preco',
                  'total', 'data_partida', 'data_chegada', 'status', 'remetente', 'remetente_nome', 'remetente_contacto',
                  'receptor', 'receptor_nome', 'receptor_contacto','rota', 'rota_descricao', 'transportador_principal', 'transportador_principal_nome',
                  'viatura_principal','viatura_principal_matricula', 'transportador_secundario',
                  'transportador_secundario_nome', 'viatura_secundaria', 'viatura_secundaria_matricula',
                  'criado_por', 'criado_por_nome', 'modificado_por', 'modficado_por_nome','criado_em', 'modificado_em']
    
    def get_tarifa_peso_preco(self, obj):
        if obj.tarifa_peso:
            return obj.tarifa_peso.preco
        return None

    def get_tarifa_volume_preco(self, obj):
        if obj.tarifa_volume:
            return obj.tarifa_volume.preco
        return None
    
    def get_remetente_contacto(self, obj):
        return obj.remetente.contacto
    
    def get_receptor_contacto(self, obj):
        return obj.receptor.contacto