<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                        >
                            <td>{{ item.product.name }}</td>
                            <td>${{ item.product.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Shipping details</h2>

                <p class="has-text-grey mb-4">* All fields are required</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>First name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Last name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Phone*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Address*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>

                        <div class="field">
                            <label>Zip code*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="zipcode">
                            </div>
                        </div>

                        <div class="field">
                            <label>Place*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="place">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength">
                    <hr>

                    <button class="button is-dark" @click="showUs">Pay with Stripe</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import PaystackPop from '@paystack/inline-js'

export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            paid_amount: '',
            reference_id: '',
            transaction_id: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | Djackets'

        this.cart = this.$store.state.cart

    /*         if (this.cartTotalLength > 0) {
                this.stripe = Stripe('pk_test_51H1HiuKBJV2qfWbD2gQe6aqanfw6Eyul5PO2KeOuSRlUMuaV4TxEtaQyzr9DbLITSZweL7XjK3p74swcGYrE2qEX00Hz7GmhMI')
                const elements = this.stripe.elements();
                this.card = elements.create('card', { hidePostalCode: true })

                this.card.mount('#card-element')
            } */
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        showUs(){
            // total = this.total
            this.$store.commit('setIsLoading', true)

            console.log('total: ', this.paid_amount * 100)

            const paystack = new PaystackPop();
                paystack.newTransaction({
                    key: 'pk_test_6c4c1910cc7c3bec582a1f61286934b35438b8ea',
                    email: this.email,
                    amount: this.paid_amount * 100,
                    currency: "NGN",
                    ref: 'FR' + Math.floor((Math.random() * 1000000000) + 1), // Generate unique reference
                    channels: ['card'],

                onSuccess: (transaction) => { 
                    // Payment complete! Reference: transaction.reference 
                    console.log('transaction: ', transaction)
                    console.log('transaction access: ', transaction.status)

                    var reference_id = transaction.reference

                    let message = 'Payment complete! Reference: ' + reference_id;
                    alert(message);

                    const items = []

                    for (let i = 0; i < this.cart.items.length; i++) {
                        const item = this.cart.items[i]
                        const obj = {
                            product: item.product.id,
                            quantity: item.quantity,
                            price: item.product.price * item.quantity
                        }

                        items.push(obj)
                    }

                    const data = {
                        'first_name': this.first_name,
                        'last_name': this.last_name,
                        'email': this.email,
                        'address': this.address,
                        'zipcode': this.zipcode,
                        'place': this.place,
                        'phone': this.phone,
                        'items': items,
                        'reference_id': reference_id,
                        'transaction_id': transaction.trans,
                        'paid_amount': this.paid_amount
                    }

                    // Verify transaction
                    axios
                        .post('/api/v1/checkout/', data)
                        .then(response => {
                            console.log('response from aerver: ', response)
                            this.$store.commit('clearCart')
                            this.$router.push('/cart/success')
                        })
                        .catch(error => {
                            this.errors.push('Something went wrong. Please try again')

                            console.log(error)
                        })

                        this.$store.commit('setIsLoading', false)
                },
                onCancel: () => {
                    // user closed popup
                }
            });

        },
        submitForm() {
            this.errors = []

            if (this.first_name === '') {
                this.errors.push('The first name field is missing!')
            }

            if (this.last_name === '') {
                this.errors.push('The last name field is missing!')
            }

            if (this.email === '') {
                this.errors.push('The email field is missing!')
            }

            if (this.phone === '') {
                this.errors.push('The phone field is missing!')
            }

            if (this.address === '') {
                this.errors.push('The address field is missing!')
            }

            if (this.zipcode === '') {
                this.errors.push('The zip code field is missing!')
            }

            if (this.place === '') {
                this.errors.push('The place field is missing!')
            }

            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                const paymentForm = document.getElementById('paymentForm');
                paymentForm.addEventListener("submit", payWithPaystack, false);
                function payWithPaystack(e) {
                e.preventDefault();
                let handler = PaystackPop.setup({
                        key: '{{ pk_public }}',
                        email: this.email,
                        amount: this.paid_amount * 100,
                        ref: 'KDBB_' + Math.floor((Math.random() * 1000000000) + 1), // Generate unique reference
                        // label: "Optional string that replaces customer email"
                        metadata: {
                            custom_fields: [
                                {
                                    display_name: "Mobile Number",
                                    variable_name: "mobile_number",
                                    value: "+2348012345678"
                                }
                            ]
                        },
                        onClose: function () {
                            alert('You are about to exit payment');
                        },
                        callback: function (response) {
                            var reference_id = response.reference

                            let message = 'Payment complete! Reference: ' + reference_id;
                            alert(message);

                            // Verify transaction
                            const currUrl = new URL('{{ request.build_absolute_uri }}')
                            currUrl.pathname = "/payment/verify/" + reference_id;
                            console.log(currUrl);
                            window.location.replace(currUrl.href)
                        }
                    });
                    handler.openIframe();
                }  
                }
            }
        },

    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                this.paid_amount += curVal.product.price * curVal.quantity
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>