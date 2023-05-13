<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('prescriptions', function (Blueprint $table) {
            $table->id();

            $table->string('drug_name');
            $table->integer('dosage');

            $table->integer('duration');
            $table->string('instructions');


            $table->unsignedBigInteger('doctor_id');
            $table->unsignedBigInteger('diagnosis_id');

            $table->foreign('doctor_id')->references('id')->on('doctors');
            $table->foreign('diagnosis_id')->references('id')->on('diagnoses');

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('prescriptions');
    }
};
