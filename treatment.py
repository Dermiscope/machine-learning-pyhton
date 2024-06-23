def find_treatment_by_acne_type(acne_type):
    treatments_data = [
        {
            "acne_type": "Bekas Jerawat",
            "treatment": "Perawatan:\nEksfoliasi Kimia: Menggunakan asam seperti asam glikolat atau asam salisilat untuk mengelupas sel kulit mati dan merangsang regenerasi kulit.\nMikrodermabrasi: Prosedur yang membantu mengurangi tampilan bekas jerawat dengan mengelupas lapisan atas kulit.\nMicroneedling: Prosedur yang menggunakan jarum-jarum kecil untuk merangsang produksi kolagen.\nKandungan yang Direkomendasikan:\nAsam glikolat\nAsam salisilat\nRetinoid (Retinol, Tretinoin)\nVitamin C\nNiacinamide"
        },
        {
            "acne_type": "Blackhead",
            "treatment": "Perawatan:\nPembersihan Rutin: Membersihkan wajah dua kali sehari dengan pembersih yang mengandung asam salisilat.\nEksfoliasi: Menggunakan scrub wajah yang lembut atau produk dengan BHA (Beta Hydroxy Acid) untuk membersihkan pori-pori.\nKandungan yang Direkomendasikan:\nAsam salisilat\nBenzoyl peroxide\nRetinoid"
        },
        {
            "acne_type": "Nodule",
            "treatment": "Perawatan:\nPengobatan Topikal: Menggunakan krim atau gel yang mengandung retinoid atau benzoyl peroxide.\nPengobatan Oral: Dalam kasus yang parah, mungkin diperlukan antibiotik oral atau isotretinoin (Accutane).\nKandungan yang Direkomendasikan:\nRetinoid\nBenzoyl peroxide\nAntibiotik (klindamisin, doksisiklin)\nIsotretinoin"
        },
        {
            "acne_type": "Papules",
            "treatment": "Perawatan:\nPembersihan Lembut: Menggunakan pembersih wajah yang lembut dan tidak menyebabkan iritasi.\nPengobatan Topikal: Menggunakan produk yang mengandung benzoyl peroxide atau asam salisilat.\nKandungan yang Direkomendasikan:\nBenzoyl peroxide\nAsam salisilat\nRetinoid"
        },
        {
            "acne_type": "Pori-Pori",
            "treatment": "Perawatan:\nEksfoliasi Rutin: Menggunakan produk dengan AHA (Alpha Hydroxy Acid) atau BHA untuk membuka pori-pori.\nPembersihan Ganda: Membersihkan wajah dengan pembersih berbasis minyak diikuti dengan pembersih berbasis air.\nKandungan yang Direkomendasikan:\nAsam salisilat\nAsam glikolat\nNiacinamide"
        },
        {
            "acne_type": "Pustule",
            "treatment": "Perawatan:\nPengobatan Topikal: Menggunakan krim atau gel yang mengandung benzoyl peroxide atau asam salisilat.\nKompres Hangat: Mengompres area yang terkena dengan air hangat untuk mengurangi peradangan.\nKandungan yang Direkomendasikan:\nBenzoyl peroxide\nAsam salisilat\nRetinoid"
        },
        {
            "acne_type": "Whitehead",
            "treatment": "Perawatan:\nPembersihan Rutin: Membersihkan wajah secara rutin dengan pembersih yang mengandung asam salisilat.\nEksfoliasi: Menggunakan produk dengan BHA untuk membersihkan pori-pori.\nKandungan yang Direkomendasikan:\nAsam salisilat\nBenzoyl peroxide\nRetinoid"
        }
    ]
    
    for treatment in treatments_data:
        if treatment["acne_type"].lower() == acne_type.lower():
            return treatment
    return None