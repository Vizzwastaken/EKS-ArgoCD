# Base image
FROM python:3
# Copy the script
COPY calculator.py /calculator.py
# Run the script
CMD ["python","/calculator.py"]
