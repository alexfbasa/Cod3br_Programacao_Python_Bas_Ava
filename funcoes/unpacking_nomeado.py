def podium(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


resultado_f1 = {'primeiro': 'Alexandre', 'segundo': 'Sarlete', 'terceiro': 'Andrea'}
podium(**resultado_f1)
