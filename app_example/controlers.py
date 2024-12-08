from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from .schemas import AuthorBase
from .functions import create_author, update_author, delete_author, list_author, retrieve_author


router = APIRouter()


@router.post(path="/author/")
async def author_create(
      					input_data: AuthorBase):
	data = await create_author(input_data)
	return JSONResponse(content=data.model_dump(), status_code=status.HTTP_201_CREATED)


@router.put(path="/author/{id_author}/")
async def author_update(
      					id_author: int,
                        input_data: AuthorBase):
	data = await update_author(id_author, input_data)
	return JSONResponse(content=data.model_dump(), status_code=status.HTTP_200_OK)


@router.delete(path="/author/{id_author}/")
async def author_delete(
      					id_author: int):
    message = await delete_author(id_author)
    return JSONResponse(content={"message": message}, status_code=200)


@router.get(path="/author/{id_author}/")
async def author_list(
						id_author: int):
	data = await retrieve_author(id_author)
	return JSONResponse(content=data.model_dump(), status_code=status.HTTP_200_OK)


@router.get(path="/author/", status_code=status.HTTP_200_OK)
async def author_list():
	data = await list_author()
	return data


@router.get(path="/middleware/")
async def middleware():
	return JSONResponse(content={"message": "Middleware"}, status_code=status.HTTP_200_OK)
