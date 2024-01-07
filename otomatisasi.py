import PySimpleGUI as sg

def calculate_total(quantity, price):
    return quantity * price

def main():
    sg.theme('LightGrey1')

    ticket_list = []

    layout = [
        [sg.Text('Nama Acara:'), sg.Input(key='event_name')],
        [sg.Text('Harga Tiket:'), sg.Input(key='ticket_price', enable_events=True)],
        [sg.Text('Jumlah Tiket:'), sg.Input(key='ticket_quantity', enable_events=True)],
        [sg.Text('Total Harga:'), sg.Text('', size=(10, 1), key='total_price')],
        [sg.Text('Nama Pembeli:'), sg.Input(key='buyer_name')],
        [sg.Button('Hitung Total'), sg.Button('Beli Tiket'), sg.Button('Tambah Acara'), sg.Button('Tambah Tiket'), sg.Button('Tampilkan Tiket'), sg.Button('Keluar')],
        [sg.Listbox(values=ticket_list, size=(30, 5), key='ticket_list')],
    ]

    window = sg.Window('Penjualan Tiket', layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Keluar':
            break
        elif event == 'Hitung Total':
            try:
                price = float(values['ticket_price'])
                quantity = int(values['ticket_quantity'])
                total_price = calculate_total(quantity, price)
                window['total_price'].update(f'${total_price:.2f}')
            except (ValueError, TypeError):
                sg.popup_error('Masukkan harga tiket dan jumlah tiket dengan benar.')
        elif event == 'Beli Tiket':
            event_name = values['event_name']
            ticket_price = float(values['ticket_price'])
            ticket_quantity = int(values['ticket_quantity'])
            total_price = calculate_total(ticket_quantity, ticket_price)
            buyer_name = values['buyer_name'] if values['buyer_name'] else 'Pembeli Tanpa Nama'
            sg.popup(f'Terima kasih kepada {buyer_name} telah membeli tiket untuk {event_name}!\nTotal Harga: ${total_price:.2f}')
            ticket_list.append(f'{buyer_name} - {event_name} - Jumlah: {ticket_quantity} - Total: ${total_price:.2f}')
            window['ticket_list'].update(values=ticket_list)
        elif event == 'Tambah Acara':
            new_event_name = sg.popup_get_text('Masukkan Nama Acara Baru:')
            if new_event_name:
                window['event_name'].update(new_event_name)
        elif event == 'Tambah Tiket':
            new_ticket = sg.popup_get_text('Masukkan Nama Tiket Baru:')
            if new_ticket:
                window['ticket_list'].update(values=ticket_list + [new_ticket])
        elif event == 'Tampilkan Tiket':
            sg.popup_ok('\n'.join(ticket_list))

    window.close()

if __name__ == '__main__':
    main()
