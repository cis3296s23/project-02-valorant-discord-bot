def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello world':
        return 'Hello human'

    if p_message == 'shop':
        return 'This feature has not been implemented. However here is a mock shop with no images because the moderator is lazy\nOni Vandal\nSmite Knife\nGaleria Bucky\nGlitchop Dagger'

    if p_message == 'help':
        return 'Currently only hello world, shop and help are the only responding messages'
    
    if p_message == 'agent':
        return 'Not yet implemented. This feature will detail in-depth information on an Agent\'s utilities. The command will likely follow as e.g. \'agent viper\''