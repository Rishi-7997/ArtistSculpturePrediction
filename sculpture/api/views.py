from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
import joblib
import os
from .serializers import SculptureSerializer

# Get the path to the pickled model file
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Model', 'Artist.pkl')

# Load the pickled model
model = joblib.load(model_path)

@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        # Deserialize the input data from the request
        serializer = SculptureSerializer(data=request.data)
        if serializer.is_valid():
            # Convert input data to input format for model
            input_data = tuple(serializer.validated_data.values())
            input_data_as_numpy_array = np.asarray(input_data)
            input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
            
            # Make a prediction using the model
            prediction = model.predict(input_data_reshaped)
            
            # Return the prediction as a JSON response
            return Response({'prediction': prediction.tolist()})
        else:
            return Response({'error': 'Invalid input data'}, status=400)
    
    return Response({'error': 'Method not allowed'}, status=405)
