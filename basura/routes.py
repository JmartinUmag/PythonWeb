from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload/")
def up_File(file: UploadFile=File(...)):
    print(file)
    return "success"