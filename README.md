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

10. Criamos um base.html. Nele temos um código como esse:

    {% block head %}{% endblock %}

    Esse código usa a sintaxe do Jinja. Conseguimos inserir esse código em outras paginas apenas fazendo que elas herdem de base!
    A boa pratica é que as paginas sigam esse formato!

11. Adicionamos SQLAlchemy (Lib) em nossa aplicação. O que significa que precisamos novamente parar a execução e buildar a imagem novamente? Sim.

12. Para solucionarmos isso de forma ideal, vamos criar um requirements.txt com:

    pip freeze > requirements.txt

13. Vamos rebuildar nossa imagem e executar novamente nosso compose, e está resolvido.

14. O Docker não sabe que algo novo foi adicionado em relação a libs. Logo apos realizar os passos acima, faça:

    docker-compose up --build

- HTML & CSS

    1. A melhor pratica para organização é você sempre deixar as partes de (posição, cor, estilo) sempre para o seu CSS (Sua pasta CSS)

    2. Sempre crie classes e referencie elas em seus elementos HTML. E essas classes você personaliza ela no seu arquivo CSS.

    3. É normal no seu compose exibir o status code: 304 Not Modified. "GET /static/css/main.css HTTP/1.1" 304 -"

    4. Esse código de status não é um erro, na real é uma resposta normal e otimizada do servidor. Ele significa:

        “O recurso requisitado (ex: o CSS main.css) não foi modificado desde a última vez que você o buscou. Pode usar o que está em cache.”