# LP ESPUMA™ — molde v1

**No ar:** https://modulo-geracao-de-imagem.vercel.app

Landing page de um infoproduto **fictício** ("curso de lavar as mãos"), feita como
demonstração do módulo de criação de LP.

## Publicar

O projeto na Vercel é `modulo-geracao-de-imagem`. Para republicar:

```bash
vercel deploy --prod --yes
vercel alias set <url-do-deploy> modulo-geracao-de-imagem.vercel.app
```

Para o deploy sair automático a cada `git push`, é preciso conectar a conta do
GitHub na Vercel uma vez (Settings → Login Connections) e depois rodar
`vercel git connect`.

## Rodar

```bash
cd ~/Desktop/lp-espuma
python3 -m http.server 8811
# abre http://localhost:8811/index.html
```

## Arquivos

```
index.html      página inteira (HTML + CSS + JS, sem dependência externa além do Google Fonts)
img/            mascote em 6 poses, blob de espuma, kit do aluno (.webp usados na LP, .png originais)
DESIGN.md       paleta, tipografia, regras do mascote e catálogo de motions
_gen.py         gerador de imagens (Nano Banana via API do Gemini)
_chroma.py      remove o fundo chroma verde e recorta o PNG
```

## Referências aplicadas

- **haoqi.design** — hero de tipografia gigante sobre objeto 3D central, grid com cruzinhas,
  HUD em fonte mono, cortina de scroll.
- **boxershorts-studio** — grão, tipografia esmagada, heading sticky nos depoimentos, pill de
  navegação flutuante, botão preto com seta.
- **CoverflowCarousel** — a seção das aulas usa o mesmo modelo do componente React, portado
  para vanilla: índice fracionário, rake com falloff, loop pelo anel, arrasto com impulso.
- **vídeo do mascote** — blob chibi de dois tons com sparkle.
- **LP de sabonete (print)** — estrutura comercial: benefício → produto → prova → oferta.

## Trocar o conteúdo

Copy, preços e depoimentos estão direto no HTML, cada seção com comentário `<!-- ===== NOME ===== -->`.
As cores saem todas das variáveis no topo do `<style>`.
