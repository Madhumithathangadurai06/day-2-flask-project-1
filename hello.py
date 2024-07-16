from flask import Flask
app=Flask('__name__')
@app.route('/')
def hello():
    return "<h1>Mother Terasa</h1>"
@app.route('/overview')
def hello1():
    return "<h1>Mother Teresa was a Catholic nun and missionary. She is famous for her charitable works and helping the poor, hungry and sick people of India. She founded the Missionaries of Charity, who ran over 500 missions worldwide. Not only that, but she was canonised as a Saint by the Catholic Church in 2016.</h1>" 
@app.route('/awards')
def hello3():
    return "<h1>The Mother Teresa Award for Corporate Citizen, , instituted in 1998, is conferred on companies that show exemplary social commitment, render service to society, care for the environment and follow scrupulously ethical principles in business. The objective of the Award, which has acquired an all India reputation and is well known in corporate circles, is to showcase a corporate which has gone far beyond its call of duty to promote welfare activities for the benefit of the poor and marginalized sections of society and is environmentally conscious.Dr. A P J Abdul Kalam, Late. Prof. C K Prahalad, Shri. M Damodaran, Prof. M S Swaminathan, Shri. Montek Singh Ahluwalia, Shri. N Gopalaswami, Shri. Gopalkrishna Gandhi, Dr. V. Shanta, Mr. N. Vaghul among others, had been our distinguished Chief Guests in the past.</h1>"
@app.route('/achievments')
def hello4():
    return "<h1>Mother Teresa is one of the most well-known recent saints in the Roman Catholic Church. She is best known for her work with the poor in Calcutta and for founding the Missionaries of Charity. St Teresa of Calcutta became renowned worldwide and even won the Nobel Peace Prize.</h1>"
@app.route('/death') 
def hello5():
    return "<h1>In 1997, her worsening health forced her permanent retirement, and the order chose an Indian-born nun, Sister Nirmala, to replace her. Mother Teresa suffered cardiac arrest and died on September 5, 1997, in Kolkata, just days after her 87th birthday.</h1>"               
if __name__=='__main__':
    app.run(debug=True)    
