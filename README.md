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