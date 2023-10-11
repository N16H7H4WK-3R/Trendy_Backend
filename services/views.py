import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import CustomUser, CartItem, Product, FavoriteItem, OrderItem
from .serializers import (
    UserSerializer,
    CartItemSerializer,
    ProductSerializer,
    FavoriteItemSerializer,
    OrderItemSerializer,
)


#####################################
######### ____User APIs____##########
#####################################


@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def user_login(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")

        user = None
        if "@" in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            data = {"token": token.key}
            return Response(data, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == "POST":
        try:
            request.user.auth_token.delete()
            return Response(
                {"message": "Successfully logged out."}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    try:
        user = request.user
        serializer = UserSerializer(
            user, data=request.data, partial=True
        )  # Allowing partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_profile(request):
    try:
        user = request.user
        user.delete()
        return Response(
            {"message": "User deleted successfully"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_user_data(request):
    try:
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#####################################
####### ____Product APIs____#########
#####################################


@api_view(["POST"])
@permission_classes([IsAdminUser])
def add_product(request):
    if request.method == "POST":
        serializer = ProductSerializer(
            data={
                "id": request.data.get("id"),
                "productPrice": request.data.get("productPrice"),
                "category": request.data.get("category"),
                "productTitle": request.data.get("productTitle"),
                "productDescription": request.data.get("productDescription"),
                "imageUrl": request.data.get("imageUrl"),
                "imageUrl1": request.data.get("imageUrl1"),
                "imageUrl2": request.data.get("imageUrl2"),
                "imageUrl3": request.data.get("imageUrl3"),
            }
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Product added successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def fetch_productData(request):
    try:
        serializer = ProductSerializer(Product.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def fetch_productDetailData(request, id):
    try:
        product = Product.objects.get(id=id)

        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#####################################
#########____Cart APIs____###########
#####################################


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    user = request.user
    product_id = request.data.get("product")

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(
            {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

    quantity = request.data.get("quantity", 1)

    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    return Response(
        {"message": "Item added to cart successfully"},
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_user_cart_data(request):
    try:
        user = request.user
        cart_items = CartItem.objects.filter(user=user)
        serializer = CartItemSerializer(cart_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_from_cart(request):
    try:
        user = request.user
        product_id = request.data.get("product")

        cart_item = CartItem.objects.filter(user=user, product=product_id).first()

        if cart_item:
            cart_item.delete()
            return Response(
                {"message": "Item removed from cart successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                {"message": "Item not found in the cart"},
                status=status.HTTP_404_NOT_FOUND,
            )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_cart_item_quantity(request):
    try:
        user = request.user
        product_id = request.data.get("product_id")
        new_quantity = int(request.data.get("quantity"))

        # Check for the item to exists in the user's cart
        cart_item = CartItem.objects.filter(user=user, product_id=product_id).first()

        if cart_item:
            if new_quantity > 0:
                cart_item.quantity = new_quantity
                cart_item.save()  # Update the cart item quantity
                serializer = CartItemSerializer(cart_item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                cart_item.delete()  # delete the cart item if quantity is 0
                return Response(
                    {"message": "Item removed from cart successfully"},
                    status=status.HTTP_204_NO_CONTENT,
                )
        else:
            return Response(
                {"message": "Item not found in the cart"},
                status=status.HTTP_404_NOT_FOUND,
            )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#####################################
#####____Favrite Item APIs____#######
#####################################


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_favorite(request):
    user = request.user
    product_id = request.data.get("product")

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(
            {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

    favorite_item, created = FavoriteItem.objects.get_or_create(
        user=user, product=product
    )

    if not created:
        favorite_item.save()

    return Response(
        {"message": "Item added to favorite successfully"},
        status=status.HTTP_201_CREATED,
    )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def remove_from_favorite(request):
    try:
        user = request.user
        product_id = request.data.get("product")

        favorite_item = FavoriteItem.objects.filter(
            user=user, product=product_id
        ).first()

        if favorite_item:
            favorite_item.delete()
            return Response(
                {"message": "Item removed from favorite successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                {"message": "Item not found in the favorite"},
                status=status.HTTP_404_NOT_FOUND,
            )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_user_favorite_data(request):
    try:
        user = request.user
        favorite_items = FavoriteItem.objects.filter(user=user)
        serializer = FavoriteItemSerializer(favorite_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#####################################
#####____Order Item APIs____#######
#####################################

# api for user's order

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_order(request):
    user = request.user
    product_id = request.data.get("product")

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(
            {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

    quantity = request.data.get("quantity", 1)

    order_item, created = OrderItem.objects.get_or_create(user=user, product=product)

    if not created:
        order_item.quantity += quantity
        order_item.save()

    return Response(
        {"message": "Item added to order successfully"},
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_user_order_data(request):
    try:
        user = request.user
        order_items = OrderItem.objects.filter(user=user)
        serializer = OrderItemSerializer(order_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def order_delivery_status(request):
    try:
        user = request.user
        product_id = request.data.get("product_id")
        new_quantity = int(request.data.get("quantity"))

        # Check for the item to exists in the user's cart
        order_item = OrderItem.objects.filter(user=user, product_id=product_id).first()

        if order_item:
            if new_quantity > 0:
                order_item.quantity = new_quantity
                order_item.save()  # Update the cart item quantity
                serializer = OrderItemSerializer(order_item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                order_item.delete()  # delete the cart item if quantity is 0
                return Response(
                    {"message": "Item removed from order successfully"},
                    status=status.HTTP_204_NO_CONTENT,
                )
        else:
            return Response(
                {"message": "Item not found in the order"},
                status=status.HTTP_404_NOT_FOUND,
            )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)