# Arquitetura e decisões técnicas

| Etapa ensinada | Implementação |
|---|---|
| Página de clientes | `data/clientes.html` |
| RPA Python/BeautifulSoup | `rpa/extract_clients.py` |
| Envio ao n8n | Webhook POST `/clientes` |
| Catálogo | CSV obtido por HTTP Request |
| Normalização | Extract From File |
| Cruzamento | Merge pelo campo `perfil` |
| MVP estático | Edit Fields cria mensagem-base |
| Desafio Plus | OpenRouter personaliza o e-mail via HTTP Request |
| Preparação | campos `to`, `subject` e `html` |
| Validação | IF com regex de e-mail |
| Envio | Gmail Send Message |

## Decisão de integração com IA

A arquitetura inicial previa um nó nativo de IA para personalizar as mensagens. Durante os testes no n8n Self-Hosted, essa configuração não concluiu a execução de maneira estável. Para preservar a funcionalidade exigida pelo desafio, a integração foi implementada com um nó **HTTP Request** conectado ao endpoint `https://openrouter.ai/api/v1/chat/completions`.

O OpenRouter utiliza o modelo `openai/gpt-4o-mini`, autenticado por uma credencial Header Auth armazenada no cofre de credenciais do n8n. A chave não é incluída no workflow exportado.

Essa alteração afeta somente o mecanismo de chamada ao modelo. O papel da IA permanece o mesmo: receber o briefing estruturado, respeitar as regras de comunicação financeira responsável e devolver o conteúdo do e-mail em HTML simples. A escolha também torna visíveis e auditáveis o endpoint, o modelo, a temperatura e o corpo da requisição.

Nos vídeos, Code nodes tratam o CSV, fazem o match e normalizam a saída. Nesta versão, essas operações usam nós nativos sempre que possível: **Split Out**, **Extract From File**, **Merge**, **Edit Fields** e **IF**. O fluxo fica mais visual, auditável e fácil de manter.

A automação não promete rentabilidade nem decide pelo cliente. O uso real requer consentimento, revisão jurídica, aprovação humana, limites de envio e monitoramento.
