from webbrowser import get

from aurora.blockchain.models import Block, Transaction
from aurora.blockchain.utils import get_address_balance, get_address_nonce
from rest_framework import mixins, views, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import BlockSerializer, TransactionSerializer


class BlockViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    """
    To handle the Blockchain requests
    """

    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class TransactionViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    """
    To handle the Transaction requests
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = self.queryset

        # filter all transactions of a block
        block_query = self.request.query_params.get("block", None)
        if block_query != None:
            block = []
            for b in Block.objects.all():
                if b.block_hash() == block_query:
                    block.append(b)
            if len(block) == 1:
                queryset = queryset.filter(block=block[0])
        return queryset

    # additional View to get the Transactions pool
    @action(detail=False)
    def pool(self, request):
        pool_transactions = Transaction.objects.filter(block=None)

        serializer = self.get_serializer(pool_transactions, many=True)
        return Response(serializer.data)


class AddressNonceView(views.APIView):
    # to get an addresses nonce (should be done by the client)
    def get(self, request, *args, **kwargs):
        return Response(get_address_nonce(self.kwargs["address"]))


class AddressBalanceView(views.APIView):
    # to get an addresses balance (should be done by the client)
    def get(self, request, *args, **kwargs):
        return Response(get_address_balance(self.kwargs["address"]))
