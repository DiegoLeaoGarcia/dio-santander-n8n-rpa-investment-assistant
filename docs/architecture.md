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
| Desafio Plus | OpenAI personaliza o e-mail |
| Preparação | campos `to`, `subject` e `html` |
| Validação | IF com regex de e-mail |
| Envio | Gmail Send Message |

Nos vídeos, Code nodes tratam o CSV, fazem o match e normalizam a saída. Nesta versão, essas operações usam nós nativos sempre que possível: **Split Out**, **Extract From File**, **Merge**, **Edit Fields** e **IF**. O fluxo fica mais visual, auditável e fácil de manter.

A automação não promete rentabilidade nem decide pelo cliente. O uso real requer consentimento, revisão jurídica, aprovação humana, limites de envio e monitoramento.
