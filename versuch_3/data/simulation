def simu(x1, y1, x2, y2, phi_1, phi_2, intervall, laenge_sim, anz_schritte_pro_ausgabe, mode): # die mode ist 0 (ohne mittelwertbildung) oder 1 (mit)
	m1 = 0.3
	m2 = 0.3
	l1 = sqrt(quadr(x1) + quadr(y1))
	l2 = sqrt(quadr(x2-x1) + quadr(y2-y1))
	phi1 = atan(-x1/y1)
	phi2 = atan((x1-x2)/(y2-y1))
	t = 0
	g = 9.81
	M = m1+m2
	phi__1 = 0
	phi__2 = 0
	zaehler = anz_schritte_pro_ausgabe
	if(mode ==1):
		while t < laenge_sim:
			if(zaehler == anz_schritte_pro_ausgabe):
				print(t, '\t', sin(phi1)*l1, '\t', -cos(phi1)*l1,'\t', sin(phi1)*l1+sin(phi2)*l2, '\t', -cos(phi1)*l1- cos(phi2)*l2)
				zaehler = 0
			zaehler += 1
			phi_1_alt = phi_1
			phi_2_alt = phi_2
			phi__1_alt = phi__1
			phi__2_alt = phi__2
			dphi = phi1 - phi2
			phi__1 = (-m2*l2*quadr(phi_2)*sin(dphi) - g*M*sin(phi1) - m2*l1*quadr(phi_1)*sin(dphi)*cos(dphi) + g*m2*sin(phi2)*cos(dphi))/(M*l1-m2*l1*quadr(cos(dphi)))
			phi__2 = (-m2*l2*quadr(phi_2)*sin(dphi)*cos(dphi)-g*M*sin(phi1)*cos(dphi)-M*l1*quadr(phi_1)*sin(dphi) + g*M*sin(phi2))/(m2*l2*quadr(cos(dphi)) - M*l2)
			phi_1 += (phi__1+phi__1_alt)/2 *intervall
			phi_2 += (phi__2_alt + phi__2)/2 * intervall
			phi1 += (phi_1 + phi_1_alt)/2 * intervall
			phi2 += (phi_2 + phi_2_alt)/2 * intervall
			t += intervall

	else:
		while t < laenge_sim:
			if(zaehler == anz_schritte_pro_ausgabe):
				print(t, '\t', sin(phi1)*l1, '\t', -cos(phi1)*l1,'\t', sin(phi1)*l1+sin(phi2)*l2, '\t', -cos(phi1)*l1- cos(phi2)*l2)
				zaehler = 0
			zaehler += 1
			dphi = phi1 - phi2
			phi__1 = (-m2*l2*quadr(phi_2)*sin(dphi) - g*M*sin(phi1) - m2*l1*quadr(phi_1)*sin(dphi)*cos(dphi) + g*m2*sin(phi2)*cos(dphi))/(M*l1-m2*l1*quadr(cos(dphi)))
			phi__2 = (-m2*l2*quadr(phi_2)*sin(dphi)*cos(dphi)-g*M*sin(phi1)*cos(dphi)-M*l1*quadr(phi_1)*sin(dphi) + g*M*sin(phi2))/(m2*l2*quadr(cos(dphi)) - M*l2)
			phi_1 += phi__1 *intervall
			phi_2 += phi__2 *intervall
			phi1 += phi_1*intervall
			phi2 += phi_2*intervall
			t += intervall
