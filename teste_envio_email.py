from servico.servico_email.enviar_email import Email


email = Email(destinatario='silva.rodrigo31@gmail.com',
              nome_arquivo='anuncio.xlsx')
email.enviar_email(assunto='Envio de email usando Orientação a OBJETO')
