def handle_uploaded_file(f):
    with open('E:\\demo_task\\sample_assignment\\demoapp\\upload'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)