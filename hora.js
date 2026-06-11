function atualizarHorario() {
    const agora = new Date();
    const hora = agora.getHours();
    const minutos = agora.getMinutes().toString().padStart(2, "0");
    const segundos = agora.getSeconds().toString().padStart(2, "0");

    let saudacao;

    if (hora >= 5 && hora < 12) {
        saudacao = "Bom dia!";
    } else if (hora >= 12 && hora < 18) {
        saudacao = "Boa tarde!";
    } else {
        saudacao = "Boa noite!";
    }

    document.getElementById("saudacao").textContent = saudacao;
    document.getElementById("hora").textContent =
        `Agora são ${hora}:${minutos}:${segundos}`;
}

atualizarHorario();
setInterval(atualizarHorario, 1000);