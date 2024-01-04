def extract_routes(file_path, output_file="routes.txt"):
    routes = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as output:
        for i, line in enumerate(lines, start=1):
            if 'route' in line.lower():
                parts = line.strip().split()
                if parts and parts[0] == '@app.route':
                    view_function = parts[-1].split('(')[0]
                    routes.append({'function': view_function, 'line': i})
                    output.write(f"Line {i}: {view_function}\n")

    return routes

if __name__ == "__main__":
    file_path = "D:/react_app/Flask-Blogging-App/blog/test/routes.py"  # Replace with the actual path to your Flask application file
    extract_routes(file_path)
