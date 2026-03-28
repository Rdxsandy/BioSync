from predict import predict_next_7_days

sample_data = [
    [7000,7,30],
    [7200,6.5,20],
    [6800,7,40],
    [7500,8,30],
    [8000,7.5,45],
    [8200,7,50],
    [8300,8,30]
]

result = predict_next_7_days(sample_data)

print(result)