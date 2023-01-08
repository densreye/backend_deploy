
def e400_BAD_RESPONSE():
    return Response({'msg':'sucedio un problema'}, status=status.HTTP_400_BAD_REQUEST)
