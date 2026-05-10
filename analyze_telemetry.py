def main():
    raw_data = [1, 2, 3, "I"]
    max_voltage = 5.0
    for data in analyze_telemetry_generator(raw_data, max_voltage):
        print(data)

def analyze_telemetry_generator(data : list, max_voltage):
    dirty_data = False
    dirty_data_list = []
    for output in data:
        try:
            yield float(output)
        except ValueError:
            dirty_data = True
            dirty_data_list.append(output)
    
    if data == dirty_data:
        yield("Data was dirty")
        for data in dirty_data_list:
            yield data
if __name__ == "__main__":
    main()