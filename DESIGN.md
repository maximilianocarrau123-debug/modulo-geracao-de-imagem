# ESPUMA™ — sistema visual (LP fictícia)

> Infoproduto 100% fictício: curso de "como lavar as mãos". Criado como demonstração
> do módulo de criação de LP. Nada aqui está à venda.

## Paleta

| token | hex | uso |
|---|---|---|
| `--yellow` | `#FFC93C` | fundo do hero, seção método, CTA final |
| `--yellow-hi` | `#FFE06A` | preenchimento de hover dos botões |
| `--amber` | `#E89611` | seção de depoimentos (amarelo queimado) |
| `--cream` | `#FBF2DE` | fundo padrão do corpo, cards |
| `--cream-d` | `#F2E3C2` | apoio |
| `--ink` | `#17130E` | tipografia, bordas, nav |
| `--dark` | `#141210` | seção de aulas e oferta |
| `--foam` | `#DDEFF7` | azul-espuma, só no FAQ (acento raro) |

## Tipografia

- **Display:** Archivo 900, `letter-spacing:-.035em`, `line-height:.83` — caixa alta, tamanho gigante.
- **Corpo:** Archivo 400/500.
- **HUD / etiquetas:** DM Mono, caixa alta, `letter-spacing:.14em`.
- **Manuscrita:** Caveat — só no kicker do hero ("o curso oficial de").

## Mascote

Blob chibi 3D, corpo dividido em duas tonalidades (amarelo manteiga + creme), olhos = dois
pontos pretos, boca = uma curva fina, sem contorno, brilho especular suave, sparkle branco
de 4 pontas. 6 poses geradas: acenando (hero), fazendo espuma, com cronômetro, com germes
(antes), comemorando (depois), com sabonete (FAQ).

Todas geradas em fundo chroma verde `#00FF00` e recortadas pelo `_chroma.py` — para gerar
pose nova, repetir o mesmo prompt-base trocando só a descrição da pose.

## Motion (o que cada efeito faz)

| efeito | onde | como |
|---|---|---|
| Cortina | hero → conteúdo | hero em `position:sticky`, escala/desfoca/some enquanto a `.stage` sobe por cima com raio de 44px |
| Parallax de camadas | hero | blob, título e mascote se movem em velocidades diferentes conforme o progresso do scroll |
| Parallax de mouse | bolhas e etiquetas | `lerp` sobre a posição do cursor, cada elemento com fator próprio (`data-float`) |
| HUD ao vivo | cantos do hero | coordenadas do mouse em fonte mono, igual à referência haoqi |
| Split por palavra | todo `h1`/`h2` | palavras fatiadas por `TreeWalker`, cada uma sobe de dentro de um `overflow:hidden` com atraso em cascata |
| Marquee reativo | 2 faixas | rola sozinho e acelera conforme a velocidade do scroll; direções opostas |
| Coverflow 3D | as 7 aulas | carrossel em perspectiva: a posição é um índice fracionário e inclinação, recuo e opacidade saem da distância até o centro (`rotate 44°`, `depth .6`, `falloff .56`). O loop dobra a distância pelo caminho mais curto do anel — sem clonar card. Arrasto com impulso, setas, teclado e dots |
| Passos sticky | método | mascote fixo troca de pose conforme o passo ativo (IntersectionObserver com margem de 45%) |
| Texto em arco | antes/depois | `textPath` em SVG girando devagar |
| Botão-tecla magnético | todos os CTAs | tecla 3D: borda inferior grossa + chão sólido (`0 6px 0`), sobe no hover (`8px`, escala 1.02) e afunda no clique (`+4px`, chão de `2px`, escala .98) com curva de mola. O magnetismo continua: o botão persegue o cursor por `--mx`/`--my`, enquanto o afundar usa `--press`/`--scale` — variáveis separadas para os dois não brigarem pelo mesmo transform |
| Grão | página inteira | `feTurbulence` em SVG inline, `mix-blend-mode:multiply`, deslocando em 6 passos |

### Variantes de tecla

| classe | fundo | chão | onde |
|---|---|---|---|
| `.btn` | tinta | preto | sobre amarelo (hero, CTA final) |
| `.btn--yellow` | amarelo | âmbar escuro `#A8690A` | sobre creme (oferta) |
| `.btn--ghost` | creme | tinta | secundário |

## Não fazer

- Não usar mais de um acento por tela (o azul-espuma só aparece no FAQ).
- Não colocar contorno no mascote nem mudar a divisão de dois tons.
- Não tirar o aviso de produto fictício do rodapé, do FAQ e do bloco de números.
