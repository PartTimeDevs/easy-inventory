FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

# ADDING DEPENDENCIES PREREQUISITES
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp \
    gcc libc-dev libffi-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

# COPY POETRY DEPENDENCIES FILES
COPY ./poetry.lock /poetry.lock
COPY ./pyproject.toml /pyproject.toml

# INSTALLING POETRY
RUN pip install --upgrade pip --user &&  \
    pip install poetry==1.1.4 &&  \
    poetry config virtualenvs.create false

# INSTALLING DEPENDENCIES
RUN poetry install --no-dev

# REMOVING DEPENDENCIES PREREQUISITES
RUN apk del .tmp

# CREATING AND USING WORKDIR
RUN mkdir /app
COPY ./app /app
WORKDIR /app
COPY ./scripts /scripts
COPY ./.env /.env

# MAKING SCRIPTS EXECUTABLE
RUN chmod +x /scripts/*

# CREATING MEDIA AND STATIC FOLDERS
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# CREATING USER, GIVE PERMISSIONS AND SWITCH TO IT
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

# RUN SH FILE
CMD ["entrypoint.sh"]
