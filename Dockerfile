# Base image
FROM python:3
# Copy the script
WORKDIR /app
COPY calculator.py /app
# Run the script
CMD ["python","/calculator.py"]
