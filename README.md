Tutorial

1. Explicando trecho de código:

    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')

    Precisamos do: host='0.0.0.0' para expormos o servidor para fora do container!
    Porque vamos executar via Docker.

2. Qual comando para eu buildar o Dockerfile?

    docker build -t nome_que_voce_quer_dar_a_sua_imagem .

3. Qual comando para executar minha aplicação via Docker?

    docker run -p 5000:5000 nome_da_sua_imagem

4. Criemos a pasta 'templates' para podermos criar nossos arquivos htmls e renderizar em nosso app.py.

    from flask import Flask, render_template

    return render_template('index.html')

5. Criemos também a pasta 'static' que ficará com nossos CSS.

6. Sempre que realizar uma alteração, se for rodar no Docker, você precisara buildar a imagem novamente.

7. Para evitar o rebuild, podemos montar um volume local no container. Isso evita que precisemos rebuildar sempre que tem uma alteração.

8. Optamos por fazer isso direto em nosso compose. Então criamos o nosso docker-compose

9. Eu quero que ele observe as mudanças na minha pasta static, templates e app.y. por isso fiz aqueles volumes no meu compose.

    volumes:
      - ./app.py:/app/app.py
      - ./static:/app/static
      - ./templates:/app/templates