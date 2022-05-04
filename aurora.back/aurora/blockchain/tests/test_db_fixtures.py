import pytest
from aurora.blockchain import models
from django.db import IntegrityError

"""
This was implemented to check if the test fixures respectively the models work, but isn't used at the moment, because the dumped data are obsolete.

"""

# @pytest.mark.dbfixture
# @pytest.mark.parametrize(
#     "id, nonce, from_address, to_address, amount, fee",
#     [
#         (
#             1,
#             0,
#             "asdf",
#             "qwer",
#             0,
#             0,
#         ),
#     ],
# )
# def test_inventory_category_dbfixture(
#     db,
#     db_fixture_setup,
#     id,
#     nonce,
#     from_address,
#     to_address,
#     amount,
#     fee,
# ):
#     result = models.Transaction.objects.get(id=id)
#     assert result.nonce == nonce
#     assert result.from_address == from_address
#     assert result.to_address == to_address
#     assert result.amount == amount
#     assert result.fee == fee
#     assert (
#         result.transaction_hash()
#         == "284503a9ac680598486526b0a3f4bb0dc8ee6982de92c160e07d7435d0c2d663"
#     )
